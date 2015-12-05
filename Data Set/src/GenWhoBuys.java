import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Random;

public class GenWhoBuys extends AbstractGen {
	
	public GenWhoBuys(Random randomGenerator, String table, String[] userComments, String[] pairings, HashMap<Integer, ArrayList<String>> eventIngred) throws IOException {
		String hardcoded = "CREATE TABLE " + table + " (email VARCHAR(256) NOT NULL REFERENCES Registered_User(email), ingredient_name VARCHAR(256) NOT NULL REFERENCES Ingredient(ingredient_name), eid INTEGER NOT NULL REFERENCES Event(eid), bringing INTEGER NOT NULL, user_comments VARCHAR(400), PRIMARY KEY(email, ingredient_name, eid));";
		HashSet<String> triplets = new HashSet<String>();
		
		// CHANGE TABLE SIZE HERE!!!
		int PRODUCTION_SIZE = 20000;
		// CHANGE TABLE SIZE HERE!!!
		
		StringBuilder sBuilder = new StringBuilder(hardcoded + "\n");
		for (int i = 0; i < PRODUCTION_SIZE; i++) {
			int pairingChoice = randomGenerator.nextInt(pairings.length);
			String[] data = pairings[pairingChoice].split("', ");
			String email = data[0];
			int eid = Integer.parseInt(data[1]);
			if (eventIngred.containsKey(eid)) {
				ArrayList<String> ingredients = eventIngred.get(eid);
				int ingredChoice = randomGenerator.nextInt(ingredients.size());
				String triplet = email + "', '" + ingredients.get(ingredChoice) + "', " + eid;
				if (!triplets.contains(triplet)) {
					triplets.add(triplet);
					int commentIndex = randomGenerator.nextInt(userComments.length * 5);
					String comments = "NULL";
					if (commentIndex < userComments.length - 1) {
						comments = "'" + userComments[commentIndex] + "'";
					}
					int bringing = randomGenerator.nextInt(6) + 1;
					sBuilder.append("INSERT INTO " + table + " VALUES('" + triplet + ", " + bringing + ", " + comments + ");\n");
				}
			}
		}
		
		myData = sBuilder.toString();
	}
	
	@Override
	protected String[] extractData() {
		return null;
	}
}