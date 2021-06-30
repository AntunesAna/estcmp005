-module(ring). %anel
-export([send/2]). %enviar

%Envia M mensagens através de um anel de N processos.
%processo principal
send(M, N) ->
  %cria uma estatística para o tempo de execução
  statistics(runtime),
  % a variável H recebe uma lista contendo a criação de um link para o processo gerado para a função anônima
  %que chama o processo loop. Em seguida, retorna o valor do processo atual e chama uma lista de sequencia
  %de tamanho N decrementando -1 até que o tamanho seja igual a 2.
  %É retornado a quantidade de processos gerados em determinado tempo.
  %calcula-se o tempo de execução novamente e envia uma mensagem de H para M, por último, a função loop é chamada
  %novamente com o parâmetro 1 no id, para que seja encerrado o processo.
  H = lists:foldl(
    fun(Id, Pid) -> spawn_link(fun() -> loop(Id, Pid, M) end) end,
    self(),
    lists:seq(N, 2, -1)),
  {_, Time} = statistics(runtime),
  io:format("~p processes spawned in ~p ms~n", [N, Time]), %N processos gerados
  statistics(runtime),
  H ! M,
  loop(1, H, M).

loop(Id, Pid, M) -> %processo secundário
  receive %recebe uma mensagem
    %Se id = 1 a variável Time recebe a estatica de tempo de execução e é retornado na tela 
    %a quantidade de mensagens geradas em um determinado tempo.
    1 ->
      {_, Time} = statistics(runtime),
      io:format("~p messages sent in ~p ms~n", [M, Time]), %M mensagens enviadas
      exit(self(), ok);
    %Se for diferente de 1, o index é decrementado e a função 
    %loop é chamada recursivamente até que o Id seja 1
    Index ->
      Pid ! Index - 1,
      loop(Id, Pid, M)
  end.
  
  
  
  %rodar no terminal
  %erl
  %c(ring).
  %ring:send(M,N).
