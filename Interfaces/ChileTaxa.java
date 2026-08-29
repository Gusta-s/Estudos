package Exercicios.Interfaces;

public class ChileTaxa implements TaxaGeral {

    @Override
    public double calcularTaxa(double taxa) {
        return (taxa / 100);
    }
    
}
