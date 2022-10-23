"""
MIT License

Copyright (c) 2022 Gabriel Costa Andrade

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sqlite3

banco = sqlite3.connect("Dados.db")
cursor = banco.cursor()

""" 
- CRIEI A TABELA DE CADASTRO DE FUNCIONÁRIOS 
- INSERI OS DADOS 
"""
#cursor.execute("CREATE TABLE Funcionarios (idCodigo integer, priNome text,segNome text, UltNome text, DataNasci text, CPF text,RG text, Endereço text, CEP text, Cidade text, Fone integer, CodDepartamento integer, Funcao text, Salario real)")
#cursor.execute("INSERT INTO Funcionarios VALUES (1,'GABRIEL', 'COSTA', 'ANDRADE', '28/12/1993', '058.694.075-83', '14254184-22', 'Rua Leonel Curvelo 117', '49050-485', 'Aracaju', 79996576727, 1, 'Diretor', 5000)")
#cursor.execute("INSERT INTO Funcionarios VALUES (2,'NADJA', 'MARIA', 'VASCONCELOS','15/02/1961', '770.234.671-72', '224455', 'Rua P M S da costa barros  58', '57036-840', 'Maceió', 82993031421, 3, 'Atendente', 2200)")
#cursor.execute("INSERT INTO Funcionarios VALUES (3,'WILLIAMS', 'SANTOS', 'COSTA', '13/12/1964', '515.789.994-72', '124423', 'Rua Professora M S Costa Barros 58', '57036-840', 'Maceió', 8233254048, 3, 'Atendente', 2200)")
#cursor.execute("INSERT INTO Funcionarios VALUES (4,'JULIEL', 'ANDRADE', 'SILVA', '18/05/1958', '117.327.685-87', '900234', 'Rua Leonel Curvelo 117', '49050-485', 'Aracaju', 79988427477, 5, 'Chefe de Estoque', 2800)")
#cursor.execute("INSERT INTO Funcionarios VALUES (5, 'WEDJA', 'COSTA', 'ANDRADE', '06/12/1969', '314.744.105-01', '67546', 'Rua Leonel Curvelo 117', '49050-485', 'Aracaju', 79996027478, 3, 'Atendente', 2200)")
#cursor.execute("INSERT INTO Funcionarios VALUES (6, 'JOAQUIM', 'COSTA', 'BARROS', '03/12/1995', '990.321.667-00', '67423', 'Avenida Jatiúca 90','57040-120', 'Maceió', 82999998877, 2, 'Administrador', 3500)")
#cursor.execute("INSERT INTO Funcionarios VALUES (7,'DAYANE', 'MENDONÇA', 'ANDRADE', '25/09/1991', '059.231.673-09','090675-11', 'Rua do Bugiu 100', '49500-001', 'Aracaju', 79991192344, 5, 'Despachante', 1500)")
#cursor.execute("INSERT INTO Funcionarios VALUES (8,'BRUNA', 'MENDONÇA', 'ANDRADE', '23/09/1994', '055.567.213-20','88734-99', 'Rua do Bugiu 102', '49500-001', 'Aracaju', 79988289829, 5, 'Despachante', 1500)")
#cursor.execute("INSERT INTO Funcionarios VALUES (9,'KIN', 'MELO', 'TORRES', '19/03/1990', '344.556.212-80','145673','Avenida da Bali Pajuçara 42', '57700-123', 'Maceió', 82981057224, 5, 'Despachante', 1500)")
#cursor.execute("INSERT INTO Funcionarios VALUES (10,'WALLACE', 'SANTOS', 'COSTA', '14/01/1959', '119.236.222-09', '554364', 'Rua do Bio 3', '56090-900', 'Maceió', 82999001440, 5, 'Motorista', 2000)")
#banco.commit()


""" 
A) Listar nome e sobrenome ordenado por sobrenome
"""
cursor.execute("SELECT priNome, UltNome FROM Funcionarios ORDER BY UltNome ASC")
a = cursor.fetchall()
print(f"\033[1:31mA saída de A:\033[m")
for x in a:
    print(x)
print(f"-=-"*40)


"""
B) Listar todos os campos de funcionários ordenados por cidade
"""
cursor.execute("SELECT * FROM Funcionarios ORDER BY Cidade ASC")
b = cursor.fetchall()
print(f"\033[1:31mA saída de B:\033[m")
for x in b:
    print(x)
print(f"-=-"*40)


"""
C) Liste os funcionários que têm salário superior a R$ 1000,00 ordenados pelo nome completo
"""
cursor.execute("SELECT priNome, SegNome, UltNome, Salario FROM Funcionarios WHERE Salario > 1000 ORDER BY priNome")
c = cursor.fetchall()
print(f"\033[1:31mA saída de C:\033[m")
for x in c:
    print(x)
print(f"-=-"*40)


"""
D) Liste a data de nascimento e o primeiro nome dos funcionários ordenados do mais novo para o mais velho
"""
cursor.execute("SELECT DataNasci, priNome FROM Funcionarios ORDER BY DataNasci ASC")
d = cursor.fetchall()
print(f"\033[1:31mA saída de D:\033[m")
for x in d:
    print(x)
print(f"-=-"*40)


'''
E) Liste o total da folha de pagamento
'''
sql = """ SELECT SUM(Salario)
FROM Funcionarios
"""
cursor.execute(sql)
e = cursor.fetchall()
print(f"\033[1:31mTotal da folha de pagamento:\033[m",end=' ')
for x in e:
    print("R$ {:.2f}".format(x[0]))
print(f"-=-"*40)


""" 
- CRIEI A TABELA DE DEPARTAMENTOS
"""
#cursor.execute("CREATE TABLE Departamentos (idDepartamentos integer PRIMARY KEY, nomeDepartamento text)")


"""
-INSERINDO DADOS NA TABELA DAPARTAMENTOS
"""
listadedepartamentos=[('1','DIREÇÃO'),
                      ('2','ADMINISTRAÇÃO'),
                      ('3','ATENDENTES'),
                      ('4','ESTOQUE'),
                      ('5','DESPACHANTES')]

#cursor.executemany("""INSERT INTO Departamentos VALUES (?,?)""", listadedepartamentos)
#banco.commit()


"""
F) Liste o nome, o nome do depatarmento, e a função de todos funcionarios 
"""

sql = """SELECT 
  Funcionarios.priNome,
  Departamentos.nomeDepartamento,
  Funcionarios.Funcao
FROM Departamentos
INNER JOIN Funcionarios ON Funcionarios.CodDepartamento = Departamentos.idDepartamentos"""
cursor.execute(sql)
f = cursor.fetchall()

print(f"\033[1:31mA saída da letra F:\033[m")
for x in f:
    print(x)
print(f"-=-"*40)


"""
G) Liste a quantidade de funcionários dessa empresa 
"""
sql = """ SELECT COUNT(priNome)
FROM Funcionarios
"""
cursor.execute(sql)
g = cursor.fetchall()

print(f"\033[1:31mO total de funcionários:\033[m", end=' ')
for x in g:
    print(x[0])
print(f"-=-"*40)


"""
H) Liste o nome do departamento e do funcionário ordenado por departamento e funcionário
"""
sql = """SELECT
   Departamentos.nomeDepartamento,
   Funcionarios.priNome
FROM Departamentos
INNER JOIN Funcionarios ON Funcionarios.CodDepartamento = Departamentos.idDepartamentos ORDER BY nomeDepartamento"""
cursor.execute(sql)

print(f"\033[1:31mA saída de H:\033[m")
h = cursor.fetchall()
for x in h:
    print(x)
