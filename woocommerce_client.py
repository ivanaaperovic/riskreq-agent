"""
woocommerce_client.py
---------------------
Modul za rad sa EKSTERNIM PODACIMA (zahtev: integracija sa eksternim servisom).

Kaci se na WooCommerce prodavnicu (lokalni CreatorLab sajt) preko zvanicnog
WooCommerce REST API-ja i dovlaci proizvode (kurseve).

Autentikacija ide preko OAuth 1.0a (consumer key/secret), sto je standard
za WooCommerce REST API preko HTTP-a.
"""

from __future__ import annotations

from typing import Any

from woocommerce import API

from config import Settings


class WooCommerceError(Exception):
    """Greska pri komunikaciji sa WooCommerce prodavnicom."""


class WooCommerceClient:
    """Tanak omotac oko WooCommerce REST API-ja."""

    def __init__(self, settings: Settings):
        self._settings = settings
        self._api = API(
            url=settings.wc_url,
            consumer_key=settings.wc_consumer_key,
            consumer_secret=settings.wc_consumer_secret,
            version="wc/v3",
            # Salji kljuceve kao query parametre - neophodno za HTTP/localhost.
            query_string_auth=True,
            timeout=settings.request_timeout,
        )

    def fetch_products(self, per_page: int = 100) -> list[dict[str, Any]]:
        """
        Dovuci sve objavljene proizvode (kurseve) iz prodavnice.

        Vraca listu recnika (sirovi JSON iz API-ja).
        Podize WooCommerceError ako sajt nije dostupan ili API vrati gresku.
        """
        try:
            response = self._api.get("products", params={"per_page": per_page})
        except Exception as exc:  # npr. ConnectionError ako sajt nije upaljen
            raise WooCommerceError(
                "Ne mogu da se povezem na WooCommerce prodavnicu.\n"
                f"   URL: {self._settings.wc_url}\n"
                "   Da li je sajt pokrenut? (start-site.sh -> http://localhost:8080)\n"
                f"   Detalj: {exc}"
            ) from exc

        if response.status_code == 401:
            raise WooCommerceError(
                "WooCommerce je odbio autentikaciju (401). "
                "Proveri WC_CONSUMER_KEY / WC_CONSUMER_SECRET u .env."
            )
        if response.status_code != 200:
            raise WooCommerceError(
                f"WooCommerce API je vratio gresku {response.status_code}: "
                f"{response.text[:200]}"
            )

        try:
            data = response.json()
        except ValueError as exc:
            raise WooCommerceError(
                "Neocekivan odgovor od WooCommerce-a (nije validan JSON)."
            ) from exc

        if not isinstance(data, list):
            raise WooCommerceError(f"Neocekivan format odgovora: {data}")

        return data

    def test_connection(self) -> bool:
        """Brza provera da li prodavnica odgovara (koristi se na startu)."""
        self.fetch_products(per_page=1)
        return True
