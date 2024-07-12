# 👋 Bem-vindo(a) ao nosso repositório, colega! 

## 📌Antes de começar...

Criei uma playlist com video-aulas rápidas sobre o assunto. **POR FAVOR,** assista todos os vídeos antes de prosseguir. Também recomendo anotar os comandos do Git. 

❤ Qualquer dúvida, pode mandar um _AJUDE-ME_ no bate-papo da nossa comunidade. Atenciosamente, Bianca Moreira. ❤

### **💡Conhecimentos Fundamentais:** 

> PlayList: https://youtube.com/playlist?list=PLNJZSGkhpAlVEEE9KzZ8642ElbxNAVDnk&si=VTMrsU9bhzDQxsD4

- O que é o Framework Django;
- O que é Git e Git Flow;
- Como trabalhar com o GitHub;
- Criar um Ambiente Virtual e instalar o Django.

**🛑IMPORTANTE🛑:** Nós estamos usando um **AMBIENTE VIRTUAL**. Ele, basicamente, empacota todas as dependências que um projeto precisa e armazena em um diretório (pasta), fazendo com que nenhum pacote seja instalado diretamente no sistema operacional (globalmente no seu computador). Sendo assim, há algumas extensões que recomendo instalarem no VS Code...

### **💡Extensões indicadas:**

>No VS Code: Ctrl+Shift+X para abrir o menu e pesquise as extensões listadas abaixo.

- Live Share: https://youtu.be/c-P4qydJC64?si=i72C3C4IMCw6gqtG&t=108
- Pyhton Environment Manager: https://youtu.be/qJRjm2HZz0M?si=M9TgQGJGJkcTgH5R&t=315 
- Material Icon Themes (coloca icones para identificação de arquivos, pastas, etc.)

## 📌Lições rápidas do Git Flow

>Para não gerar confusões, deixarei aqui a descrição de alguns comandos importantes do *Git Flow*, e algumas recomendações. 


>Nunca use comandos com _finish_ enquanto uma branch estiver em desenvolvimento, caso contrário, essa branch irá se mesclar com a branch develop. Converse com seus colegas antes de fazer isso.

#### 🔎Branches de Produção:

- **Main:** A principal, a versão publicada e funcional do projeto. Alterações **NÃO** são feitas diretamente nela.
- **Develop:** A branch de desenvolvimento, é a partir dela que criamos novas branches chamadas _features_ para fazer alterações.

**Você precisa:**

- Ter uma conta no GitHub;
- Ter "clonado" o repositório da turma no seu PC;
- Ter assistido a video-aula  _"Trabalhando em equipe com Git Flow
"_ da playlist.


#### 🔎Identificação: 
>Primeira coisa que você deve fazer no terminal do git.

    git config --global user.email "seu email do Github"

em  seguida:

    git config --global user.name "seu nome de usuário do Github"