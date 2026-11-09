# Como ativar o agente do Instagram

**Ativado em 09/11/2026.** Este guia fica como registro, caso seja preciso refazer. É tudo grátis.

**Nunca cole o token ou a senha em uma conversa.** Eles vão direto nos campos indicados abaixo.

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

Feito em 09/11/2026. Fica registrado aqui caso seja preciso refazer.

A conta do Instagram precisa ser **profissional**, de criador ou empresa. Apps novos da Meta não têm mais o "login do Instagram", então o caminho é o **login unificado**.

1. Em **developers.facebook.com**, crie o app `Bolso Fila` com o caso de uso **Gerenciar mensagens e conteúdo no Instagram**.
2. Em **Casos de uso**, **Personalizar**, **API setup with Unified login**, ligue o app ao portfólio **helo_gois**.
3. Em **Funções do app**, adicione **bolsodesenhado** como **Testador do Instagram** e aceite o convite no Instagram, em `instagram.com/accounts/manage_access/`.
4. De volta ao login unificado, no passo 1, toque em **Criar nova configuração** e depois em **Criar do modelo**. O token dessa configuração **nunca expira**.
5. No passo 2, toque em **Gerar token** na linha da **bolsodesenhado** e autorize. Se pedir uma Página do Facebook, pode escolher qualquer uma sua: o token não publica em páginas.

## Parte 3: guardar o token no GitHub

No repositório, abra **Settings**, **Secrets and variables**, **Actions** e toque em **New repository secret**.

- **Name:** `IG_TOKEN`. **Secret:** cole o token da Meta. Salve.

Para conferir sem publicar nada: em **Actions**, abra **Conferir token** e toque em **Run workflow**. O registro deve mostrar `token OK em https://graph.facebook.com: conta @bolsodesenhado`.

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
- O token não vence. Ele só para de funcionar se você remover o app **Bolso Fila** ou tirar a @bolsodesenhado dele. Nesse caso, gere outro e substitua o `IG_TOKEN`.
