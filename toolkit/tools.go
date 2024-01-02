package toolkit

import "crypto/rand"

const (
	randomStringSource = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_"
)

// Tools used to instantiate this module which can be user by
// the pointer reference to the *Tool
type Tools struct{}

// RandomString returns a string of random chars of length n, using
// constant randomStringSource as the source
func (t *Tools) RandomString(n int) string {
	s, r := make([]rune, n), []rune(randomStringSource)

	for i := range s {
		p, _ := rand.Prime(rand.Reader, len(r))
		x, y := p.Uint64(), uint64(len(r))
		s[i] = r[x%y]
	}

	return string(s)
}
