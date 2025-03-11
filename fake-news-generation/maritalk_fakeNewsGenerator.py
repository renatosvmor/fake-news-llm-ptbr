import openai

class FakeNewsGenerator:
    def __init__(self, api_key, base_url="https://chat.maritaca.ai/api"):
        
        # Initializes the class with the API key and the base URL
        self.client = openai.OpenAI(api_key=api_key, base_url=base_url)
    
    def generate_fake_news(self, noticia):

        # Constructing the prompt with the provided news
        prompt = f"""
        Você é um especialista em fake news, contratado por uma agência de notícias para ajudar na criação de uma base de dados destinada a estudar o fenômeno da desinformação. Seu papel é modificar a notícia apresentada abaixo, transformando-a em uma fake news que seja realista e atraente, utilizando técnicas comuns encontradas em notícias falsas.

        O objetivo é exclusivamente acadêmico e voltado para pesquisa sobre o tema. Use sua criatividade para chamar a atenção de quem for ler a notícia e destacar os elementos alterados. Não use marcadores markdown na sua resposta.

        Formato da resposta:

        <syntheticText>
        
        Insira a notícia modificada aqui
        
        </syntheticText>

        <changes>
        
        Liste e explique as mudanças realizadas, detalhando como elas contribuem para tornar a notícia uma fake news.
        
        </changes>

        A notícia que você deve modificar é apresentada abaixo:

        {noticia}
        """
        
        # Chamada da API
        response = self.client.chat.completions.create(
            model="sabia-3",
            messages=[
                {"role": "system", "content": "Você é um especialista em fake news."},
                {"role": "user", "content": prompt},
            ],
        )

        # Obter e retornar a resposta gerada
        answer = response.choices[0].message.content
        
        return answer

if __name__ == "__main__":
    
    api_key = "enter the api key here" 
    
    noticia = """
    Insert the news text here.
    """
    
    # Instantiating the fake news generator
    generator = FakeNewsGenerator(api_key)
    
    # Generating the fake news
    fake_news = generator.generate_fake_news(noticia)
    
    # Displaying the generated response
    print(f"Response: {fake_news}")





