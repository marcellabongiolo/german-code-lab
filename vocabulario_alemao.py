"""Gerenciador de vocabulário em alemão.

O módulo mantém uma pequena base local de substantivos em alemão e permite
consultar artigo, plural e significado em português.
"""

VOCABULARIO = {
    "Softwareentwicklung": {
        "artigo": "die",
        "plural": "Softwareentwicklungen",
        "significado": "Desenvolvimento de software",
    },
    "Wissenschaft": {
        "artigo": "die",
        "plural": "Wissenschaften",
        "significado": "Ciência",
    },
    "Architektur": {
        "artigo": "die",
        "plural": "Architekturen",
        "significado": "Arquitetura",
    },
    "Schlüssel": {
        "artigo": "der",
        "plural": "Schlüssel",
        "significado": "Chave",
    },
}


class GerenciadorVocabularioAlemao:
    """Consulta exemplos de vocabulário alemão."""

    def __init__(self, vocabulario=None):
        self.vocabulario = vocabulario if vocabulario is not None else VOCABULARIO.copy()

    def consultar_termo(self, termo: str) -> str:
        """Retorna uma ficha formatada para um termo conhecido."""
        termo_limpo = termo.strip()

        if not termo_limpo:
            raise ValueError("O termo não pode estar vazio.")

        termo_normalizado = next(
            (
                palavra
                for palavra in self.vocabulario
                if palavra.casefold() == termo_limpo.casefold()
            ),
            None,
        )

        if termo_normalizado is None:
            return f"O termo '{termo_limpo}' ainda não foi cadastrado no laboratório."

        dados = self.vocabulario[termo_normalizado]
        artigo = dados["artigo"]
        return (
            f"Termo: {artigo} {termo_normalizado}\n"
            f"Plural: {dados['plural']}\n"
            f"Significado: {dados['significado']}"
        )


def main() -> None:
    """Executa uma demonstração do gerenciador."""
    sistema = GerenciadorVocabularioAlemao()
    termos_para_testar = [
        "Softwareentwicklung",
        "Architektur",
        "Schlüssel",
        "Python",
    ]

    print("=" * 60)
    print("GERMAN CODE LAB")
    print("=" * 60)

    for palavra in termos_para_testar:
        print(f"\nBuscando por: '{palavra}'")
        print(sistema.consultar_termo(palavra))
        print("-" * 40)


if __name__ == "__main__":
    main()
