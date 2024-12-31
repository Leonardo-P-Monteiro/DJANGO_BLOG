# O que é o Git? 
R: É um software de gerenciamento das versões do código. 

# O que é o Github? 
R: Github é uma "rede social" onde posso fazer upload dos meus projetos para evitar que 
eles fiquem hospedados na minha máquina. Penso no seu funcionamento igual ao Google Drive.

# Estagios do commit
- modified: indica que o arquivo foi alterado. 
- staging: indica que os arquivos estão prontos para serem "comitados". 
- committed: indica que os arquivos foram "comitados".

# Comando para atualizar o Git pelo terminal do windows.
    git update-git-for-windows

# Comando para iniciar (criar) o git na pasta do projeto.
    git init

# Comando para adicionar arquivos no stage de mudanças. 
    git add nome_arquivo.
    git add . --> para adicionar todos os arquivos de uma vez só.

# Comando para fazer o commit.
    git commit -m "título do commit"
    git commit -m "título do commit" -m "texto descritivo"

# Comando para ver o status dos arquivos em relação ao processo de commits.
    git status

# Comando para obter o histórico de commits.
    git log
    git log --oneline (esse é muito resumido)

# Comandos para visualizar os arquivos.
    git checkout nº do commit. --> Aqui vamos apenas visualizar sem reverter os arquivos.
                               --> Se eu quiser posso criar uma branch aqui ou retornar pra esse ponto e manter o restante das modificações.
                               --> Para retornar ao estágio mais atual do arquivo basta digitar o comando e inserir o código do último commit ou digitar o nome da branch.
                               --> DÊ PREFERÊNCIA A ESSE MÉTODO, ELE É MAIS SEGURO.

##    ---- Explicação via IA. ---

    git checkout	Muda o contexto para um branch específico ou restaura um arquivo para um estado anterior.
    
    git revert	Cria um novo commit que desfaz as alterações de um commit anterior, mantendo o histórico limpo.
    
    git reset	Move o ponteiro do branch para um commit específico, podendo descartar commits ou reescrevê-los. 
                Use com cautela, pois pode levar à perda de dados se usado incorretamente.

# Arquivo .env --> É um arquivo que contém variáveis de sistema que utilizamos em nosso projeto. 
É um arquivo que não deve ser "comitado" no Github. Para isso usamos um outro arquivo padrão que, tudo que estiver escrito dentro dele, não será feito upload.
        
        --> .gitignore

# Aquivo .gitignore --> É um arquivo que vai armazenar os nomes dos arquivos/pastas que desejo não serem commitados. 

O git vai acessar esse arquivo e não vai fazer upload de todos os arquivos que tiverem listados nele.


# Comando para cirar/visualizar as branchs existentes e criar branchs novas.
    git branch --> Nos permite visualizar as branchs 
    git branch nome_arquivo --> Nos permite criar uma nova branch.

# Comando para renomear uma branch:
    git branch -m 'novo_nome_branc' --> Importante lembrar que para renomear a branch é preciso que estejamos na branch que desejamos renomear.

# Comando para trocar de branch.
    git checkout nome_branch --> Mesmo que utilizamos para retornar a arquivos.

# Comando para fundir uma branch com a branch principal.
    git merge nome_branch --> Importante dizer que para fundir a banch ramificada ao branch principal é necessário que primeiro mudemos para o branch principal e depois executemos o comando seguido do nome da branch secundária que queremos unir ao branch principal.

# Comando para deletar uma branch:
    git branch -d nome_branch --> Se houve arquivos a serem comitados ele não permite ser deletado.
    git branch -D nome_branch --> Nesse aqui ele vai deletar à força, ainda que haja arquivos a serem comitados.



# Comandos para subir (upload) baixar (download) nossos códigos no Github

    git push link_diretorio_github nome_branch --> remete nossos commits para o GitHub.
    
    git pull link_diretorio_github nome_branch --> faz download de todas as alterações que foram realizadas no diretório que está no GitHub.

# Remover o Git à força (Cudidado! apagará a pasta inteira do git).
    $ rm -rf .git --> Apaga apenas a pasta do git, projeto permanece normal.

# Renomear o branch atual de 'feature-x' para 'nova-feature'
    git branch -m nova-feature


# Configurando para ficar automático o envio do commit quando usar o comando git push origin.
    git remote --add link_repositorio_github


# Copiando um projeto/repositório do GitHub para o meu computador.

Para realizar esse procedimento fazemos uso do comando 'git clone link_repositorio'.
> git clone link_repositorio

# Comando para "puxar" as atualizaçoes do projeto que está no GitHub.

'git pull origin'

# Pull request.

Pull request é quando nós criamos uma branch diferente para trabalhar as modificações que desejamos implantar no projeto. 
Quando essas modificações estão no ponto de serem incorporadas ao projeto principal, branch main, nós fazermos o upload para o github e lá no diretório online vai ser criada uma espécie de notificação mostrando que existe essa alteração feita na branch de alterações e que ela já pode ser unida ao projeto principal. Daí o gerente de projeto é que fará a autorização ou não da fusão dessas alterações ao projeto principal.


# (Re)Definir usuário e e-mail registrados nos commits.
git config --global user.name "Seu Nome Completo"
git config --global user.email "seu_email@example.com"
