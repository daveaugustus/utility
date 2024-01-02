package toolkit

import (
	"fmt"
	"testing"
)

func TestToolsRandomString(t *testing.T) {
	var testTools Tools

	str := testTools.RandomString(16)
	fmt.Printf("str: %v\n", str)
	if len(str) != 16 {
		t.Error("Length mismatch")
	}
}
