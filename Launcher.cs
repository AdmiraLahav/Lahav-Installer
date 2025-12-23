using System;
using System.Diagnostics;
using System.IO;
class Program
{
    static void Main()
    {
        string Working_Dir = Directory.GetCurrentDirectory();
        //use a var named path to read the 
        string path=Console.ReadLine();
        string args = Console.ReadLine();
        path.ToString();
        args.ToString();
        
        using (Process processvar = new Process())
        {
            //u can use the absolute path of the file too
            processvar.StartInfo.FileName = $"{args}";
            processvar.StartInfo.Arguments = $"{args}";
            processvar.Start();
        }
    }
}