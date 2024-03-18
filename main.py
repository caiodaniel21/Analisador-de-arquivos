import os
import os.path
import sys

if len(sys.argv) < 2:
  print ('Por favor, coloque um caminho de diretório para ser analisado')
  sys.exit()

caminho = sys.argv[1]


pagina = open('tamanho_diretórios.html', 'w', enconding="utf-8")

pagina.write('''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Tamanho dos diretórios</title>
</head>
<body>
''')

for raiz, pastas, arquivo in os.walk(caminho):
  pagina.write(f'<h1> Caminho: {raiz}</h1>\n')
  tamanho_total = 0

  for p in pastas:
    caminho_total = os.path.join(raiz, p)
    tamanho_total += sum(os.path.getsize(os.path.join(caminho_total, arquivo)) for arquivo in os.listdir(caminho_total) if os.path.isfile(os.path.join(caminho_total, arquivo)))
    pagina.write(f'<p> Tamanho da pasta -{p}-: {tamanho_total} bytes\n')

  for a in arquivos:
    caminho_total = os.path.join(raiz, a)
    tamanho_total += os.path.getsize(caminho_total)
    pagina.write(f'<p> Tamanho do arquivo -{a}-: {tamanho_total} bytes\n')

pagina.write('''
</body>
</html>
''')
pagina.close()
  
