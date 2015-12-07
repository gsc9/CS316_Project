import java.io.BufferedReader;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;

public class Generator {
	
	public Generator(int seed, String[] tables) {
		Random randomGenerator = new Random(seed);
		try {
			generate(randomGenerator, tables);
		}
		catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		int seed = 0;
		String[] tables = {"Auth_User", "Event", "Ingredient", "Part_Of", "Event_Ingredient", "Who_Buys"};
		new Generator(seed, tables);
	}
	
	private void generate(Random randomGenerator, String[] tableNames) throws IOException {
		String[] randomSentences = randomSentences();
		
		AbstractGen[] tables = new AbstractGen[tableNames.length];
		tables[0] = new GenAuthUser(randomGenerator);
		
		String[] usernames = tables[0].extractData();
		
		tables[1] = new GenEvent(randomGenerator, tableNames[1], randomSentences);
		tables[2] = new GenIngredient(tableNames[2]);
		
		String[] eids = tables[1].extractData();
		String[] ingredients = tables[2].extractData();
		
		tables[3] = new GenPartOf(randomGenerator, tableNames[3], usernames, eids);
		tables[4] = new GenEventIngredient(randomGenerator, tableNames[4], randomSentences, eids, ingredients);
		
		String[] pairings = tables[3].extractData();
		HashMap<Integer, ArrayList<String>> eventIngred = tables[4].extractComplexData();
		
		tables[5] = new GenWhoBuys(randomGenerator, tableNames[5], randomSentences, pairings, eventIngred);
		
		String path = System.getProperty("user.dir");
		FileWriter writer = new FileWriter(path + File.separator + "GEN-PRODUCTION.SQL");
		for (int i = 1; i < tables.length; i++) {
			writer.write(tables[i].myData + "\n");
		}
		writer.flush();
		writer.close();
		
		writer = new FileWriter(path + File.separator + "admin.py");
		writer.write(tables[0].myData);
		writer.flush();
		writer.close();
	}
	
	private String[] randomSentences() throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(this.getClass().getResourceAsStream("/resources/Random Sentences.txt")));
		StringBuilder sBuilder = new StringBuilder();
		String line = in.readLine();
		while (line != null) {
			sBuilder.append(line + "\n");
			line = in.readLine();
		}
		in.close();
		return sBuilder.toString().split("\n");
	}
}