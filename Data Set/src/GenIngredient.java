import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class GenIngredient extends AbstractGen {
	
	private String[] myIngredients;
	
	protected GenIngredient(String table) throws IOException {
		myHardcoded = "CREATE TABLE " + table + " (ingredient_name VARCHAR(256) NOT NULL PRIMARY KEY);\n";
		
		BufferedReader in = new BufferedReader(new InputStreamReader(this.getClass().getResourceAsStream("/resources/Food.txt")));
		StringBuilder sBuilder = new StringBuilder();
		StringBuilder iBuilder = new StringBuilder();
		String line = in.readLine();
		while (line != null) {
			sBuilder.append("INSERT INTO " + table + " VALUES('" + line + "');\n");
			iBuilder.append(line + "\n");
			line = in.readLine();
		}
		in.close();
		
		myIngredients = iBuilder.toString().split("\n");
		myData = sBuilder.toString();
	}
	
	@Override
	protected String[] extractData() {
		return myIngredients;
	}
}