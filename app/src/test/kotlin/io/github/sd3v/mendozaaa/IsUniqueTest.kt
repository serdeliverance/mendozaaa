package io.github.sd3v.mendozaaa

import org.junit.Test
import kotlin.test.assertFalse
import kotlin.test.assertTrue

internal class IsUniqueTest {

    @Test
    fun whenLettersAreDifferentItShouldReturnBeTrue() {
        val result = isUnique("adc")
        assertTrue { result }
    }

    @Test
    fun whenHavingSingleLetterItShouldReturnTrue() {
        val result = isUnique("b")
        assertTrue { result }
    }

    @Test
    fun whenHavingRepeatedLettersItShouldReturnFalse() {
        val result = isUnique("ajeuu")
        assertFalse { result }
    }
}