fun main(args: Array<String>) {

    val a = 2.3
    val b = 4
    val c = 5.6
    val root1: Double
    val root2: Double
    val output: String

    val determinant = b * b - 4.0 * a * c 

    if (determinant > 0) {
        root1 = (-b + Math.sqrt(determinant)) / (2 * a)
        root2 = (-b - Math.sqrt(determinant)) / (2 * a)

        output = "root1 = %2.f and roo2 = %.2f" .format(root1, root2)
    }

    else if (determinant == 0.0) {
        root2 = -b / (2 * a)
        root1 = root2

        output = "root1 = root2 = %.2f;".format(root1)
    }
    else {
        val realPart = -b/ (2*a)
        val imaginaryPart = Math.sqrt(determinant) / (2 * a)

        output = "root1 = %.2f+%.2fi and root2 = %.2f-%.2fi". format(realPart, imaginaryPart, realPart, imaginaryPart)
    }
    printIn(output)
}
