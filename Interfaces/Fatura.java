package Exercicios.Interfaces;
public class Fatura {
    private double pricePerHour;
    private double pricePerDay;
    private TaxaGeral taxa;

    public Fatura(double pricePerHour, double pricePerDay, TaxaGeral taxa) {
        this.pricePerHour = pricePerHour;
        this.pricePerDay = pricePerDay;
        this.taxa = taxa;
    }

    public Fatura(double pricePerHour, double pricePerDay) {
        this.pricePerHour = pricePerHour;
        this.pricePerDay = pricePerDay;
    }
    public Fatura(){
    }

    public double getPricePerHour() {
        return pricePerHour;
    }

    public void setPricePerHour(double pricePerHour) {
        this.pricePerHour = pricePerHour;
    }

    public double getPricePerDay() {
        return pricePerDay;
    }

    public void setPricePerDay(double pricePerDay) {
        this.pricePerDay = pricePerDay;
    }

    public TaxaGeral gettaxa() {
        return taxa;
    }
    public void setTaxa(TaxaGeral taxa){
        this.taxa = taxa;
    }

    //eu sei que isso tá feio, mas é 00:45 e eu tô caindo de sono
    public double processarFatura(double pricePerDay, double pricePerHour){
        if (pricePerDay <= 24) {
            return(pricePerDay + pricePerHour) * taxa.calcularTaxa(20) + pricePerDay + pricePerHour;
        }
        else {
            return (pricePerDay + pricePerHour) * taxa.calcularTaxa(10) + pricePerDay + pricePerHour;
        }
    }
    
}