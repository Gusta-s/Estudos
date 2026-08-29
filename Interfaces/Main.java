package Exercicios.Interfaces;
public class Main {
    public static void main(String[] args) {
        Fatura f = new Fatura(1,24,new BrasilTaxa());
        Fatura fc = new Fatura(1,24, new ColombiaTaxa());
        Fatura fch = new Fatura(1,24, new ChileTaxa());
        //(24 + 1) * (0.20 + 1) + 24 + 1
        System.out.println(f.processarFatura(24, 1));
        //(24 + 1) * (0.20 + 3) + 24 + 1
        System.out.println(fc.processarFatura(24, 1));
        //(24 + 1) * 0.20 + 24 + 1
        System.out.println(fch.processarFatura(24, 1));
    }
    
}