class Lasagna
{
    public int ExpectedMinutesInOven(){
        return 40;
    }

    public int RemainingMinutesInOven(int elapsedTime){
        return ExpectedMinutesInOven() - elapsedTime;
    }

    public int PreparationTimeInMinutes(int layers){
        return layers * 2;
    }

    public int ElapsedTimeInMinutes(int layers, int elapsedTime){
        return PreparationTimeInMinutes(layers) + elapsedTime;
    }
}
