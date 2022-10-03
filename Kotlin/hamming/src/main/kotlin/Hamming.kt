object Hamming {
    fun compute(leftStrand: String, rightStrand: String): Int {
        var count = 0
        var len = leftStrand.length
        if (len != rightStrand.length){
            throw IllegalArgumentException("left and right strands must be of equal length")
        }
        if (len == 0){
            return 0
         } else {
            for (i in 0..len - 1){
                if (leftStrand[i] != rightStrand[i]){
                    count += 1
                }
            }
            return count
        } 
    }
}