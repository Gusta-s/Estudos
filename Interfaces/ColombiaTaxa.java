package Exercicios.Interfaces;

public class ColombiaTaxa implements TaxaGeral{

    @Override
    public double calcularTaxa(double taxa) {
        
        return (taxa /100) + 3;
    }
    
}
