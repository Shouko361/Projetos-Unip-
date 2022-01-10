// See https://aka.ms/new-console-template for more information
namespace Study { 
    
    class Variaveis { 
        static void Main() {

            Console.WriteLine("Hello World!"); // Exibição de texto no console
            

                        
            int x = 4;      // Declaração de variavel do tipo int
            double y = 3.3; // Declaração de variavel do tipo double (ou float)

            double area = x * y; // Declaração de variavel que tera como conteudo o resultado de uma operação matematica de outras duas variaveis
            
            Console.WriteLine("A area do quadrado é " + area); // Exibição do resultado da variavel responsavel pela operação matematica
            

            
            double b = x; // Conversão Implicita
            Console.WriteLine(y);

            double nota = 8.6;
            int notaconvertida = (int)nota; // Conversão Explicita
            Console.WriteLine(notaconvertida);
            
            
            
            Console.WriteLine("Escreva o numero de sua casa: ");
            string numeroCasa = Console.ReadLine();
            int numero = int.Parse(numeroCasa);
            Console.WriteLine("O numero da sua casa é: {0}", numero); //{0} é para indicar a posição da primeira variavel a ser informada dentro de Console.WriteLine dentro da string

            numero = Convert.ToInt32(numeroCasa);

            Console.WriteLine(numero);
            

            
            double z = 20.232;
            Console.WriteLine(z.ToString("F2")); // F1 ou F2 e assim por diante = numero de casas decimais do numero 
            Console.WriteLine(z.ToString("C")); // C = Cash = Apresenta a variavel em valor monetario
            Console.WriteLine(z.ToString("P")); // P = Percentage = Apresenta a variavel em porcentagem
            

            
            Console.WriteLine("Qual seu nome?");
            String name = Console.ReadLine();
            Console.WriteLine("Qual sua idade?"); // Entrada de dados pelo usuario
            int age = int.Parse(Console.ReadLine()); // Lê a linha de codigo anterior e atribui a variavel int age (Parse faz a conversão da entrada de string para int)

            Console.WriteLine("Seu nome é {0} e sua idade é de {1} anos", name, age);
            

            
            var idade = 25;    // Aqui as variaveis são definidas pelo programador (eu)
            var sal = 1285.76; // e o proprio programa decide suas tipagens (int e float)

            Console.WriteLine("Idade: {0}. Salario: {1}", idade, sal);



            int c = 2;

            Math.Pow(c, 2); // Aqui a variavel c esta sendo elevada ao quadrado (c²)
            Console.WriteLine("O resto da divisão de c/2 é igual a " + (c % 2)); // Aqui esta sendo apresentado o resto da divisão de c/2
            

            double nota1 = 8;
            double nota2 = 9;

            Console.WriteLine("Nota 1 maior que 7? {0}", nota1 > 7); // Operação booleana para verificar se o valor dado é maior que 7, responde com true ou false
            Console.WriteLine("Nota 2 igual a dez? {0}", nota2 == 10); // Operação booleana para verificar se o valor dado é igual a 10, responde com true ou false
            

            // se o aluno passou por média, se ele foi reprovado (nota menor que 4) ou se está em recuperação (nota menor que 6).

            Console.WriteLine("Digite a nota 1: ");
            string strnota1 = Console.ReadLine();
            Console.WriteLine("Digite a nota 2: ");
            string strnota2 = Console.ReadLine();
            int nota3 = Int32.Parse(strnota1); // Conversão da entrada de dados
            int nota4 = Int32.Parse(strnota2); // pelo usuario de string para int
            float media = ((nota3 + nota4) / 2);

            // Estrutura condicional para checagem da situação do aluno
            if (media <= 4)
                Console.WriteLine("Aluno reprovado");
            else if (media > 4 && media <= 6)
                Console.WriteLine("Aluno em recuperação");
            else
                Console.WriteLine("Aluno aprovado");
            
            
            var X = false;
            var n1 = 6;
            var n2 = 5;
            var n3 = 7;
            var n4 = 8;

            Console.WriteLine(!X); // Aqui é apresentado o contrario da variavel X
            n3++;                  // Aqui é adicionado +1 ao valor de n3
            Console.WriteLine(n3); 
            n4--;                  // Aqui é subtraido -1 do valor de n4
            Console.WriteLine(n4);

            Console.WriteLine(n2 == --n1);   // Aqui é apresentado o resultado de se n2 é igual a n1 sendo subtraido -1 do valor atual de n1
            Console.WriteLine(n2-- == ++n1); // Aqui e apresentado o resultado de se n2 é igual a n1 sendo subtraido -1 do valor atual de n2 e adicionado +1 ao valor atual de n1
            
            
            var n5 = 5;
            var n6 = 9;
            var n7 = 10;

            // Exemplo de estrutura condicional
            if (n5 < n6) {
                Console.WriteLine("Condição 1 é satisfeita!");
                Console.WriteLine("Resultado da soma é {0}", n5 + n6);
            }
            else
            {
                Console.WriteLine("Condição 1 não é satisfeita!");
            }

            if (n7 < n6) {
                Console.WriteLine("Condição 2 é satisfeita");
                Console.WriteLine("Resultado da soma é {0}", n7 + n6);
            }
            else{
                Console.WriteLine("Condição 2 não é satisfeita!");
            }
          
            
            // Estrutura Switch
            Console.WriteLine("Em qual a nota você avalia o nosso prato?");
            int.TryParse(Console.ReadLine(), out int nota5);

            switch (nota5){
                case 0:
                    Console.WriteLine("Comida muito ruim!");
                    break;
                case 5:
                    Console.WriteLine("Comida Razoavel");
                    break;
                case 10:
                    Console.WriteLine("Comida muito boa!");
                    break;
                default:
                    Console.WriteLine("Nota inexistente");
                    break;
            }
            
            
            // Estrutura While
            var n8 = 1;

            while (n8 <= 15)
            {
                Console.WriteLine(n5);
                n8++;
            }
            

            // Estrutura For
            int n9 = 1;
            for (n9 = 1; n9 <= 10; n9++)
            {
                Console.WriteLine(n9);
            }
            
        }
    
    }

    class atv1
    {
        static void Main()
        {
            bool i = true;
            while (i == true)
            {
                Console.WriteLine("Insira a nota do primeiro trimestre: ");
                float.TryParse(Console.ReadLine(), out float n1);
                Console.WriteLine("Insira a nota do segundo trimestre: ");
                float.TryParse(Console.ReadLine(), out float n2);
                Console.WriteLine("Insira a nota do terceito trimestre: ");
                float.TryParse(Console.ReadLine(), out float n3);

                float media = ((n1 + n2 + n3) / 3);

                if (media < 7)
                {
                    Console.WriteLine("Aluno em recuperação");
                    i = false;
                }
                else if (media >= 7)
                {
                    Console.WriteLine("Aluno aprovado");
                    i = false;
                }
                else
                {
                    Console.WriteLine("Nota inexistente, para refazer a entrada de notas pressione 0 e confirme");
                    int.TryParse(Console.ReadLine(), out int repeat);
                    if (repeat == 0)
                    {
                        i = true;
                    }
                    else
                    {
                        i = false;
                    }
                }
            }
        }

    }
    
    class atv2
    {
        static void Main()
        {
            bool i = true;
            while (i == true)
            {
                float result = 0;
                Console.WriteLine("Insira aqui o primeiro numero");
                float.TryParse(Console.ReadLine(), out float n1);
                Console.WriteLine("Insira aqui o segundo numero");
                float.TryParse(Console.ReadLine(), out float n2);
                Console.WriteLine("Qual a operação desesada?");
                string opnf = Console.ReadLine();
                string op = opnf.ToUpper();

                if (op == "SOMA" || op == "MAIS" || op == "+")
                {
                    result = (n1 + n2);
                    Console.WriteLine("O resultado é {0}", result);
                    i = false;
                }
                else if (op == "SUBTRAÇÃO" || op == "MENOS" || op == "-")
                {
                    result = (n1 - n2);
                    Console.WriteLine("O resultado é {0}", result);
                    i = false;
                }
                else if (op == "MULTIPLICAÇÃO" || op == "VEZES" || op == "*" || op == "x")
                {
                    result = (n1 * n2);
                    Console.WriteLine("O resultado é {0}", result);
                    i = false;
                }
                else if (op == "DIVISÃO" || op == "DIVIDIDO" || op == "/")
                {
                    result = (n1 / n2);
                    Console.WriteLine("O resultado é {0}", result);
                    i = false;
                }
                else
                {
                    Console.WriteLine("Valores ou operador aritimetico incorreto, tente novamente");
                }
            } 
        }
    }
}