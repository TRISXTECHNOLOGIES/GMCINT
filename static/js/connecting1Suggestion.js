
  // Sample array of suggestions
  const suggestionsConnt1 = [
    
"Afghanistan:Kabul Hamid Karzai International Airport (Kabul) - IATA: KBL",
"Albania:Tirana International Airport (Tirana) - IATA: TIA",
"Algeria:Houari Boumediene Airport (Algiers) - IATA: ALG",
"Angola:Quatro de Fevereiro Airport (Luanda) - IATA: LAD",
"Antigua and Barbuda:V.C. Bird International Airport (Antigua) - IATA: ANU",
"Argentina:Ezeiza Ministro Pistarini International Airport (Buenos Aires) - IATA: EZE",
"Armenia:Zvartnots International Airport (Yerevan) - IATA: EVN",
"Australia:Sydney Kingsford Smith Airport (Sydney) - IATA: SYD",
"Austria:Vienna International Airport (Vienna) - IATA: VIE",
"Salzburg Airport (Salzburg) - IATA: SZG",
"Innsbruck Airport (Innsbruck) - IATA: INN",
"Azerbaijan:Heydar Aliyev International Airport (Baku) - IATA: GYD",
"Bahamas:Lynden Pindling International Airport (Nassau) - IATA: NAS",
"Bahrain:Bahrain International Airport (Manama) - IATA: BAH",
"Bangladesh:Shahjalal International Airport (Dhaka) - IATA: DAC",
"Barbados:Grantley Adams International Airport (Bridgetown) - IATA: BGI",
"Belarus:Minsk National Airport (Minsk) - IATA: MSQ",
"Belgium:Brussels Airport (Brussels) - IATA: BRU",
"Antwerp International Airport (Antwerp) - IATA: ANR",
"Liege Airport (Liege) - IATA: LGG",
"Belize:Philip S. W. Goldson International Airport (Belize City) - IATA: BZE",
"Benin:Cotonou Cadjehoun Airport (Cotonou) - IATA: COO",
"Bhutan:Paro International Airport (Paro) - IATA: PBH",
"Bolivia:Viru Viru International Airport (Santa Cruz) - IATA: VVI",
"Bosnia and Herzegovina:Sarajevo International Airport (Sarajevo) - IATA: SJJ",
"Botswana:Sir Seretse Khama International Airport (Gaborone) - IATA: GBE",
"Brazil:Sao Paulo-Guarulhos International Airport (Sao Paulo) - IATA: GRU",

  ];

  const inputField = document.getElementById("connectingLeavingFrom");
  const suggestionBox = document.getElementById("suggestion-box-Connet-1");

  // Add event listener for input field
  inputField.addEventListener("input", function () {
      const userInput = this.value.toLowerCase();
      suggestionBox.innerHTML = ""; // Clear previous suggestions
      suggestionBox.classList.add("hidden"); // Hide suggestion box by default

      if (userInput) {
          // Filter suggestions based on user input
          const filteredSuggestions = suggestionsConnt1.filter(suggestion =>
              suggestion.toLowerCase().includes(userInput)
          );

          // If there are suggestions, display them
          if (filteredSuggestions.length > 0) {
              filteredSuggestions.forEach(suggestion => {
                  const suggestionItem = document.createElement("div");
                  suggestionItem.textContent = suggestion;
                  suggestionItem.classList.add("p-2", "cursor-pointer");

                  // Add hover effect
                  suggestionItem.addEventListener("mouseover", function () {
                      suggestionItem.classList.add("bg-gray-200");
                  });

                  suggestionItem.addEventListener("mouseout", function () {
                      suggestionItem.classList.remove("bg-gray-200");
                  });

                  // Fill input with suggestion on click
                  suggestionItem.addEventListener("click", function () {
                      inputField.value = suggestion;
                      suggestionBox.innerHTML = ""; // Clear suggestions
                      suggestionBox.classList.add("hidden"); // Hide suggestion box
                  });

                  suggestionBox.appendChild(suggestionItem);
              });

              suggestionBox.classList.remove("hidden"); // Show suggestion box
          }
      }
  });

  // Hide suggestion box when clicking outside
  document.addEventListener("click", function (event) {
      if (!inputField.contains(event.target)) {
          suggestionBox.innerHTML = ""; // Clear suggestions
          suggestionBox.classList.add("hidden"); // Hide suggestion box
      }
  });
