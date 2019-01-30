using System;

namespace Fibonacci
{
    class Program
    {
        static int Fibonacci(int num)
        {
            if (num <= 0) return 0;
            if (num == 1) return 1;
            return Fibonacci(num - 1) + Fibonacci(num - 2);
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Adj meg egy számot");
            int szam = Int32.Parse(Console.ReadLine());

            Console.WriteLine(Fibonacci(szam));
            Console.ReadKey();
        }
    }
}
