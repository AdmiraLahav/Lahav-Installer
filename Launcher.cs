using System;
using System.Diagnostics;
using System.Security.Cryptography.X509Certificates;
class Program
{
    static void Main()
    {
        //use a var named path to read the 
        string path=Console.ReadLine();
        path.ToString();
        using (Process processvar = new Process())
        {
            //u can use the absolute path of the file too
            processvar.StartInfo.FileName = $"{path}";
            processvar.Start();
        }
    }
}