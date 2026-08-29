package Exercicios.Interfaces;
public class Main {
    public static void main(String[] args) {
        Fatura f = new Fatura(1,24,new BrasilTaxa());
        System.out.println(f.processarFatura(24, 1));  
    }
    
}