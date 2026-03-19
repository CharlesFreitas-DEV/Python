<hr/>

<p>Este repositório serve de suporte ao estudo da linguagem Python fornecendo diversos exemplos nas mais diversas aplicações.</p>

<p>A depender do exemplo a ser estudado, algumas bibliotecas deverão ser instaladas. Para isso deverá ser utilizado o instalador de pacotes PIP. Vejamos como utilizá-lo.</p>

<hr/>

<h3>PIP</h3>

<p>Primeiro devemos verificar o PIP está instalado.</p>

<pre><code>pip --version</code></pre>

<p>Caso ele não esteja instalado,ele pode ser baixado e instalado a partir da URL a seguir:</p>

<pre><a target='_blank' href='https://pypi.org/project/pip/'>https://pypi.org/project/pip/</a></pre>

<p>Caso ele já esteja instalado é sempre aconselhável atualizar a versão do PIP:</p>

<pre><code>python -m pip install --upgrade pip</code></pre>

<p>Uma vez atualizado, utilizamos o comando PIP para instalar a biblioteca desejada:</p>

<pre><code>pip install <i>nome_biblioteca</i></code></pre>

Onde <i>nome_biblioteca</i> é o nome da biblioteca que se deseja instalar.

<p>Caso haja algum controle de permissão de usuário que impossibilite a instalação da biblioteca, devemos adicionar o argumento <i>--user</i>:</p>

<pre><code>pip install <i>nome_biblioteca</i> --user</code></pre>

Em cada pasta serão descritas as bibliotecas usadas nos exemplos.
