Diretriz 3.1.1 - Negócios - Pagamentos - Compras no Aplicativo

Descrição do Problema:

 Notamos que o aplicativo inclui ou acessa conteúdo, serviços ou funcionalidades digitais pagos por meios que não sejam a Compra no Aplicativo, o que não é apropriado para a App Store. Especificamente: 

- O aplicativo ainda acessa conteúdo digital adquirido fora do aplicativo, como um plano de assinatura, mas esse conteúdo não está disponível para compra por meio da Compra no Aplicativo. 

Aplicativos na loja dos Estados Unidos podem incluir links para o navegador padrão, usando botões, links externos ou outras chamadas para ação, para mecanismos de pagamento que não sejam a Compra no Aplicativo. Para saber mais, consulte a publicação de notícias no Apple Developer . Para lojas onde não há opções alternativas para aplicativos qualificados , o aplicativo deve usar a Compra no Aplicativo. 

Próximos Passos:

 O conteúdo, os serviços ou as assinaturas digitais pagos incluídos ou acessados ​​pelo aplicativo devem estar disponíveis para compra no aplicativo por meio da Compra no Aplicativo. 

Aplicativos que oferecem serviços e conteúdo digital pagos em várias plataformas podem permitir que os clientes acessem o conteúdo adquirido fora do aplicativo, desde que ele também esteja disponível para compra por meio da Compra no Aplicativo. Consulte a diretriz 3.1.3(b) para obter mais informações. 

Caso tenha informações adicionais a fornecer sobre o conteúdo e os serviços digitais do aplicativo e como as diretrizes se aplicam a eles, responda a esta mensagem no App Store Connect e nos informe. Se houver alguma informação que você gostaria que considerássemos em nossa análise de futuros envios, sinta-se à vontade para incluí-la na seção "Informações de Análise do App" do App Store Connect.
Diretriz 2.5.4 - Desempenho - Requisitos de Software

Descrição do Problema:

 O aplicativo declara suporte para áudio na chave UIBackgroundModes do arquivo Info.plist, mas não conseguimos reproduzir nenhum conteúdo audível quando o aplicativo está em execução em segundo plano. 

O áudio em segundo plano destina-se ao uso por aplicativos que fornecem conteúdo audível ao usuário enquanto estão em segundo plano, como reprodutores de música, aplicativos de criação musical ou aplicativos de streaming de áudio. 

Próximos Passos

 : Se o aplicativo tiver um recurso que exija áudio persistente, responda a esta mensagem e adicione uma gravação de tela mostrando o uso do áudio persistente em segundo plano em um dispositivo físico. Navegue até a Tela Inicial para mostrar o modo de segundo plano em uso na gravação. Inclua a gravação no campo "Notas" da seção "Informações de Análise do Aplicativo" no App Store Connect para envios futuros. 

Se o aplicativo não tiver um recurso que exija áudio persistente, seria apropriado remover a configuração "audio" da chave UIBackgroundModes. 