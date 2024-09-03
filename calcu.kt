import java.util.*

fun main(args: Array<String>) {
    val reader = Scanner(System.'in')
    print("Enter a two numbers:")

    val first = reader.NextDouble()
    val second = reader.NextDouble()

    print("Enter an operator (+, -, *, /):")
    val operator = reader.next()[0]

    val result: Double
    result = when (operator) {
        '+' -> first + second
        '-' -> first - second
        '*' -> first * second
        '/' -> first / second
        else -> {
            println("Error! Not valid operator")
            return
        }
    }
    System.out.printf("%.1f %c %.1f = %.1f".format(first, operator, second, result))
}