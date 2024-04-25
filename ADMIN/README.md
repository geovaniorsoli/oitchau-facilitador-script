# Facilitador para registro de ponto na plataforma Oitchau

Este é um conjunto de scripts desenvolvidos para facilitar o processo de registro de ponto na plataforma Oitchau. Os scripts foram criados para aguardar o tempo de espera em horários de pico, como entrada às 8h, intervalo para almoço às 12h e retorno do almoço às 13h, bem como a saída às 18h.

Para mais detalhes e instruções de uso, acesse a [documentação](https://oitchau-facilitador.vercel.app/).

## Scripts disponíveis

- `auto`: Script principal que ao executar e realiza a marcação de ponto na plataforma Oitchau.
- `autoIntervalo`: Script que ao executar, aguarda o tempo necessário para a paginar carregar, bate o ponto e bloqueia o computador.
- `autoSaida`: Faz a mesma coisa que autoIntervalo, porém desliga o seu computador.

## Linguagens e bibliotecas

- **Python**: Linguagem de programação utilizada para desenvolver os scripts.
- **Selenium**: Biblioteca utilizada para interagir com o navegador web e automatizar ações na plataforma Oitchau.
- **PyInstaller**: Utilizado para criar executáveis dos scripts Python para facilitar a execução em diferentes ambientes.

---
Este projeto é uma iniciativa para otimizar o processo de registro de ponto na plataforma Oitchau, tornando-o mais eficiente e conveniente para os usuários. Se tiver alguma dúvida ou sugestão, sinta-se à vontade para contribuir ou entrar em contato com a equipe de desenvolvimento.
