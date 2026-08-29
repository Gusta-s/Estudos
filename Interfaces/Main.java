package Exercicios.Interfaces;
public class Main {
    public static void main(String[] args) {
        Fatura f = new Fatura();
        BrasilTaxa tax = new BrasilTaxa();
        tax.setTaxa(10);
        System.out.println(f.processarFatura(24, 1, tax));        
    }
    
}