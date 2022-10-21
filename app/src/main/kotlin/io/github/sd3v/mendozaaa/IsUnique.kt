package io.github.sd3v.mendozaaa

fun isUnique(string: String): Boolean {

    if (string.length <= 1) {
        return true
    }

    val sorted = string.toCharArray().sorted().joinToString("")

    var i = 1

    while (i < sorted.length) {
        if (sorted[i] == sorted[i - 1]) {
            break
        }
        i++
    }

    return i >= sorted.length
}