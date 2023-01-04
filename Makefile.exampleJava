build: trial rise redemption

run_trial:
	java Trial

run_rise:
	java Rise

run_redemption:
	java Redemption

trial: Trial.java Task.java
	javac $^

rise: Rise.java Task.java
	javac $^

redemption: Redemption.java Task.java
	javac $^

clean:
	rm -f *.class

.PHONY: build clean
