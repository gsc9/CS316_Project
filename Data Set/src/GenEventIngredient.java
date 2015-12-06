import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;

public class GenEventIngredient extends AbstractGen {
	
	private HashMap<Integer, ArrayList<String>> myComplexData;
	
	public GenEventIngredient(Random randomGenerator, String table, String[] hostComments, String[] eids, String[] ingredients) throws IOException {
		myHardcoded = "CREATE TABLE " + table + " (id INTEGER NOT NULL UNIQUE PRIMARY KEY, ingredient_name VARCHAR(256) NOT NULL REFERENCES Ingredient(ingredient_name), eid INTEGER NOT NULL REFERENCES Event(eid),  quantity INTEGER NOT NULL, units VARCHAR(256), comments VARCHAR(256), UNIQUE(ingredient_name, eid));\n";
		myComplexData = new HashMap<Integer, ArrayList<String>>();
		int[] quantities = {1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 18, 20, 24};
		String[] units = {"NULL", "NULL", "NULL", "NULL", "NULL", "'lbs'", "'kg'", "'bags'", "'cans'", "'packets'"};
		
		// CHANGE TABLE SIZE HERE!!!
		int PRODUCTION_SIZE = 20000;
		// CHANGE TABLE SIZE HERE!!!
		
		StringBuilder sBuilder = new StringBuilder();
		for (int i = 0; i < PRODUCTION_SIZE; i++) {
			int commentIndex = randomGenerator.nextInt(hostComments.length * 5);
			String comments = "NULL";
			if (commentIndex < hostComments.length - 1) {
				comments = "'" + hostComments[commentIndex] + "'";
			}
			int ingredChoice = randomGenerator.nextInt(ingredients.length - 1);
			int eventChoice = randomGenerator.nextInt((eids.length * 2) / 3);
			if (!myComplexData.containsKey(eventChoice + 1)) {
				ArrayList<String> newList = new ArrayList<String>();
				newList.add(ingredients[ingredChoice]);
				myComplexData.put(eventChoice + 1, newList);
			}
			else {
				ArrayList<String> oldList = myComplexData.get(eventChoice + 1);
				oldList.add(ingredients[ingredChoice]);
				myComplexData.put(eventChoice + 1, oldList);
			}
			int quantityChoice = randomGenerator.nextInt(quantities.length);
			int unitChoice = randomGenerator.nextInt(units.length);
			sBuilder.append("INSERT INTO " + table + " VALUES(" + (i+1) + ", '" + ingredients[ingredChoice] + "', " + eids[eventChoice] + ", " + quantities[quantityChoice] + ", " + units[unitChoice] + ", " + comments + ");\n");
		}
		
		myData = sBuilder.toString();
	}
	
	@Override
	protected String[] extractData() {
		return null;
	}
	
	@Override
	protected HashMap<Integer, ArrayList<String>> extractComplexData() {
		return myComplexData;
	}
}