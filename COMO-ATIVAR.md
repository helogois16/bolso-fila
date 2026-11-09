# Como ativar o agente do Instagram

Leva cerca de 30 minutos e só precisa ser feito uma vez. É tudo grátis.

**Nunca cole o token, a senha ou a chave em uma conversa.** Eles vão direto nos campos indicados abaixo.

Os nomes dos botões da Meta e do GitHub mudam com o tempo. Se algum estiver diferente, me avise e eu te guio pela tela.

---

## Parte 1: GitHub

1. Crie uma conta em **github.com** e confirme o e-mail.
2. Toque no **+**, no alto da página, e depois em **New repository**.
3. Em **Repository name**, escreva `bolso-fila`.
4. Marque **Public** e não marque nenhuma outra opção.
5. Toque em **Create repository** e **me mande o endereço da página**. Eu envio os arquivos para lá.

Depois que eu enviar os arquivos:

6. No repositório, abra **Settings** e depois **Pages**.
7. Em **Source**, escolha **Deploy from a branch**. Em **Branch**, escolha **main** e a pasta **/ (root)**. Toque em **Save**.

## Parte 2: Meta (token do Instagram)

A conta do Instagram precisa ser **profissional**, de criador ou empresa.

1. Entre em **developers.facebook.com** e toque em **Meus apps**, depois em **Criar app**.
2. Dê o nome `Bolso Fila`. No caso de uso, escolha a opção de **gerenciar mensagens e conteúdo no Instagram**.
3. Dentro do app, abra **Configuração da API com login do Instagram**.
4. Em **Gerar tokens de acesso**, adicione a conta **@bolsodesenhado** e autorize com o seu login.
5. Se pedir, aceite o convite de testador no Instagram, em **Configurações**, **Apps e sites**.
6. Toque em **Gerar token** e deixe a tela aberta para a próxima parte.

## Parte 3: guardar as chaves no GitHub

No repositório, abra **Settings**, **Secrets and variables**, **Actions** e toque em **New repository secret**.

1. **Name:** `IG_TOKEN`. **Secret:** cole o token da Meta. Salve.

Agora crie a chave que mantém o token renovado:

2. Na sua foto do GitHub, abra **Settings**, **Developer settings**, **Personal access tokens**, **Fine-grained tokens** e **Generate new token**.
3. Em **Expiration**, escolha o maior prazo que aparecer e anote a data.
4. Em **Repository access**, escolha **Only select repositories** e marque `bolso-fila`.
5. Em **Permissions**, coloque **Secrets** como **Read and write**. Gere e copie.
6. Crie outro segredo no repositório. **Name:** `GH_ADMIN`. **Secret:** cole essa chave.

---

## Como funciona depois de ativado

1. Eu gero o Reel e você aprova o roteiro e as imagens.
2. Depois do vídeo aprovado, eu coloco na fila com a data e o horário.
3. O agente confere a fila a cada 15 minutos e publica o Reel com legenda e capa. O post pode sair de 5 a 30 minutos depois do horário marcado.

## O que continua na sua mão

- **Stories com adesivo** (enquete, quiz e contagem).
- **Comentário fixado:** a API não fixa comentários.
- **TikTok:** sem a auditoria do TikTok, a API só publica em modo privado.

## Quando algo der errado

O GitHub manda um e-mail avisando. Na fila (`fila.json`), o status mostra o que houve:

| Status | O que significa | O que fazer |
|---|---|---|
| `publicado` | Saiu certo | Nada |
| `conferir` | O Instagram não confirmou | Veja no perfil se saiu. O agente não repete sozinho, para não postar duas vezes |
| `atrasado` | Passou de 6 horas do horário | Escolha outra data |
| `erro` | Falhou 3 vezes | Me mande o e-mail do GitHub |

## Bom saber

- O repositório é **público**: quem tiver o endereço vê os vídeos da fila antes da hora. Nele não entram o e-book, o código de acesso nem as chaves.
- O GitHub desliga agendamentos em repositórios sem nenhum commit por **60 dias**. Se a fila ficar parada esse tempo, reative em **Actions**.
- A chave `GH_ADMIN` vence na data que você anotou. Antes disso, gere outra e substitua o segredo.
