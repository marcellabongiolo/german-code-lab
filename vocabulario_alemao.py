"""
Módulo: Processador de Vocabulário e Artigos em Alemão
Autor: Marcella Bongiolo
Descrição: Script utilitário para gerenciar substantivos em alemão, 
           validando seus artigos corretos (Der/Die/Das) e plural.
"""

class GerenciadorVocabularioAlemao:
    """Gerencia uma base de dados local de termos em alemão com regras e validações."""
    def __init__(self):
        # Dicionário estruturado: Palavra -> {"artigo": X, "plural": Y, "significado": Z}
        self.vocabulario = {
            "Softwareentwicklung": {
                "artigo": "die", 
                "plural": "Softwareentwicklungen", 
                "significado": "Desenvolvimento de software"
            },
            "Wissenschaft": {
                "artigo": "die", 
                "plural": "Wissenschaften", 
                "significado": "Ciência"
            },
            "Architektur": {
                "artigo": "die", 
                "plural": "Architekturen", 
                "significado": "Arquitetura"
            },
            "Schlüssel": {
                "artigo": "der", 
                "plural": "Schlüssel", 
                "significado": "Chave"
            }
        }

    def consultar_termo(self, termo: str) -> str:
        """Busca um termo e retorna sua ficha técnica formatada em alemão."""
        termo_formatado = termo.capitalize()
        
        if termo_formatado in self.vocabulario:
            dados = self.vocabulario[termo_formatado]
            artigo = dados["artigo"].capitalize()
            return (
                f"🇩🇪 Termo: {artigo} {termo_formatado}\n"
                f"📦 Plural: {dados['plural']}\n"
                f"💡 Significado: {dados['significado']}"
            )
        else:
            return f"⚠️ O termo '{termo}' ainda não foi cadastrado no laboratório."

def main():
    print("=" * 60)
    print(" 🥨 GERMAN CODE LAB: PROCESSADOR DE VOCABULÁRIO 📚")
    print("=" * 60)

    sistema = GerenciadorVocabularioAlemao()

    # Testando consultas com termos técnicos e do idioma
    termos_para_testar = ["Softwareentwicklung", "Architektur", "Schlüssel", "Python"]

    for palavra in termos_para_testar:
        print(f"\nBuscando por: '{palavra}'")
        print(sistema.consultar_termo(palavra))
        print("-" * 40)
           

    print("=" * 60)

if __name__ == "__main__":
    main()
Add German vocabulary manager script
