# CDC - Classificação das Doenças do Café
Classificação das Doenças do Café (CDC) é um projeto feito para conclusão de curso da UNIFEI, ele busca unir a necessidade do tratamento contínuo dos cafezais com o grande aumento no poder de processamento de microcontroladores para auxiliar pequenos produtores a aumentar a produtividade enquanto reduz os custos por meio de IA embarcada.

# Visão Geral
O projeto consiste em utilizar uma rede MobileNet embarcada em um microcontrolador com câmera e display LCD para classificar doenças presentes em folhas dos cafeeiros. Foram utilizados três datasets de outros projetos e um dataset feito usando a própria placa de desenvolvimento. 

Além disso, foram desenvolvidos dois sistemas com o intuito de comparar as performances da solução proposta. No final, a arquitetura de estágio único apresentou uma precisão de 93% quando inferida no computador e a arquitetura em cascata apresentou uma precisão de 96% quando inferida no computador. Em testes com os sistemas embarcados, a aquitetura em estágio único apresentou precisão de 71% e a arquitetura em cascata apresentou uma precisão de 82%. 

