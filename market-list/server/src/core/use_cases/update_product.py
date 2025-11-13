from typing import Optional

from src.core.entities.product import Product
from src.core.exceptions import ProductNotFound
from src.core.interfaces.product_repository import ProductRepository
from src.core.interfaces.usecase_interface import UseCase


class UpdateProductUseCase(UseCase):
    """Use case responsible for updating an existing product."""

    def __init__(self, repository: ProductRepository):
        self._repository = repository

    def execute(
        self, nomeAntigo: str, nome: str, quantidade: Optional[int], valor: float
    ) -> Product:
        if self._repository.get_by_name(nomeAntigo):
            raise ProductNotFound(f"Produto '{nomeAntigo}' não encontrado.")

        product = Product(nome=nome, quantidade=quantidade, valor=valor)
        return self._repository.update(product)