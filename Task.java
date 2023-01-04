import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public abstract class Task {
    public abstract void solve() throws IOException, InterruptedException;

    public abstract void readProblemData() throws IOException;

    public abstract void formulateOracleQuestion() throws IOException;

    public abstract void decipherOracleAnswer() throws IOException;

    public abstract void writeAnswer() throws IOException;

    public void askOracle() throws IOException, InterruptedException {
        ProcessBuilder builder = new ProcessBuilder();
        builder.redirectErrorStream(true);
        builder.command("python3", "sat_oracle.py", "sat.cnf", "sat.sol");
        Process process = builder.start();
        BufferedReader in = new BufferedReader(new InputStreamReader(process.getInputStream()));
        String buffer;
        StringBuilder output = new StringBuilder();

        while ((buffer = in.readLine()) != null) {
            output.append(buffer).append("\n");
        }

        int exitCode = process.waitFor();
        if (exitCode != 0) {
            System.err.println("Error encountered while running oracle");
            System.err.println(output.toString());
            System.exit(-1);
        }
    }
}