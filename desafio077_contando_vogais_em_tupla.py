def main():
    palavras = ('aprender', 'programar', 'linguagem', 'python',
                'curso', 'gratis', 'estudar', 'praticar', 
                'trabalhar', 'mercado', 'programador', 'futuro')

    for palavra in palavras:
        print(f'Na palavra {palavra.upper()} temos ', end='')
        for letra in palavra.lower():
            if letra in 'aeiou':
                print(letra, end=' ')
        print()

main()