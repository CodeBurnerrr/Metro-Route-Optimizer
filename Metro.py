def mindistance(distance, stat):
    length = len(stat)
    minimum = float('inf')
    ind = 0
    for k in range(length):
        if not stat[k] and distance[k] <= minimum:
            minimum = distance[k]
            ind = k
    return ind


def dijkstra(graph, source, stations):
    length = len(graph[0])
    distance = [float('inf')] * length
    stat = [False] * length
    distance[source] = 0

    for _ in range(length):
        m = mindistance(distance, stat)
        stat[m] = True
        for i in range(length):
            if not stat[i] and graph[m][i] != 0 and distance[m] != float('inf') and distance[m] + graph[m][i] < distance[i]:
                distance[i] = distance[m] + graph[m][i]

    print("Minimum Number of Stations from", stations[source], "To every station")
    print()
    for k in range(length):
        if stations[source] == stations[k]:
            continue
        else:
            print(stations[source], "--------->", stations[k], "  =  ", distance[k])

def get_final_list(station):
    intersections = []

    for i in range(len(station) - 1):
        for j in range(len(station[i])):
            common = station[i][j]
            if common in station[i + 1]:
                intersections.append(common)

    final_list = []

    for i in range(len(station)):
        for j in station[i]:
            if j in final_list:
                continue
            else:
                final_list.append(j)

    return final_list


def get_graph(final_list, station):


    final_matrix = [[0 for i in final_list] for j in final_list]
    my_dict = {key: [] for key in final_list}

    for i in range(len(station)):
        for j in range(len(station[i])):
            if j == 0:
                my_dict[station[i][j]] += [station[i][j + 1]]
            elif j == len(station[i]) - 1:
                my_dict[station[i][j]] += [station[i][j - 1]]
            else:
                my_dict[station[i][j]] += [station[i][j + 1]]
                my_dict[station[i][j]] += [station[i][j - 1]]

    for i in range(len(final_matrix)):
        temp = my_dict[final_list[i]]
        for j in range(len(final_matrix)):
            if final_list[j] in temp:
                final_matrix[i][j] = 1

    return final_matrix


def get_source_station(stations):
    print("Enter the source station:")
    for i in range(len(stations)):
        print(f"Enter {i} for {stations[i]}")
    source = int(input("Your choice: "))
    return source

def menu():
    Ahmedabad = [
        ["Thaltej Gam", "Thaltej", "Doordarshan Kendra", "Gurukul Road", "Gujarat University", "Commerce Six Road",
         "SP Stadium", "Old High Court", "Shahpur", "Ghee Kanta", "Kalupur Railway Station", "Kankaria East",
         "Apparel Park", "Amraiwadi", "Rabari colony", "Vastral", "Nirant Cross Road", "Vastral Gam"],
        ["Motera Stadium", "Sabarmati", "AEC", "sabarmati railway station", "Ranip", "Vadaj", "Vijay Nagar",
         "Usmanpura", "Old High Court", "Gandhigram", "Paldi", "Shreyas", "Rajivnagar", "Jivraj", "APMC"]
    ]

    Hyderabad = [
        ["L.B. Nagar", "Victoria Memorial", "Chaitanyapuri", "Dilsukhnagar", "Musarambagh", "New Market", "Malakpet",
         "M.G. Bus Station", "Osmania College", "Gandhi Bhavan", "Nampally", "Assembly", "Lakdi_ka_Pul", "Khairtabad",
         "Irrum Manzil", "Punjagutta", "Ameerpet", "S.R. Nagar", "ESI Hospital", "Erragadda", "Bharat Nagar",
         "Moosapet", "Balanagar", "Kukatpally", "KPHB Colony", "JNTUCollege", "Miyapur"],
        ["Falaknuma", "Shamsheer Gunj", "Shalibanda", "Charminar", "Salarjung Museum", "M.G. Bus Station",
         "Sultan Bazar", "Narayanguda", "Chikkadapally", "RTC X Roads", "Musheerabad", "Gandhi Hospital",
         "Secunderabad West", "Parade Ground"],
        ["Nagole", "Uppal", "Stadium", "NGRI", "Habsiguda", "Tarnaka", "Mettuguda", "Secunderabad East",
         "Parade Ground", "Paradise", "Rasoolpura", "Prakash Nagar", "Begumpet", "Ameerpet", "Madhura Nagar",
         "Yousufguda", "Jubilee Hills", "Jubilee Hills Check Post", "Peddamma Temple", "Madhapur", "Durgam Cheruvu",
         "Hitech city", "Rai Durg"]
    ]

    Lucknow = [
        ["Alambagh", "Alambagh ISBT", "Amausi", "Badshahnagar", "Bhootnath Market", "Charbagh",
         "CCS International Airport", "Durgapuri", "Hazratganj", "Hussainganj", "Indira Nagar", "IT Chauraha",
         "KD Singh Babu Stadium", "Krishna Nagar", "Lekhraj Market", "Lucknow University", "Mawaiya", "Munshi Pulia",
         "Sachivalaya", "Singar Nagar", "Transport Nagar"],

    ]

    Kolkata = [
        ["Kavi Subhash", "Shahid Khudiram", "Kavi Nazrul", "Gitanjali", "Masterda Surya Sen", "Netaji",
         "Mahanayak Uttam Kumar", "Rabindra Sarobar", "Kalighat", "Jatin Das Park", "Netaji Bhavan", "Rabindra Sadan",
         "Maidan", "Park Street", "Esplanade", "Chandni Chowk", "Central", "Mahatma Gandhi Road", "Girish Park",
         "Shobhabazar Sutanuti", "Shyambazar", "Belgachhia", "Dum Dum", "Noapara", "Baranagar", "Dakshineswar"],
        ["Salt Lake Sector-V", "Karunamoyee", "Central Park", "City Center", "Bengal Chemical", "Salt Lake Stadium",
         "Phoolbagan", "Sealdah", "Esplanade", "Mahakaran", "Howrah", "Howrah Maidan"],
        ["Hemanta Mukhopadhyay", "Kavi Sukanta", "Jyotirindra Nandi", "Satyajit Ray", "Kavi Subhash"],
        ["Joka", "Thakurpukur", "Sakherbazar", "Behala Chowrasta", "Behala Bazar", "Taratala", "Majerhat"]

    ]

    Chennai = [
        ["Wimco Nagar Depot", "Wimco Nagar", "Tiruvottriyur", "Tiruvottriyur Theradi", "Kaladipet", "Tollgate",
         "New Washermanpet", "Tondiarpet", "Sir Theagaraya College", "Washermanpet", "Mannadi", "High Court",
         "Puratchi Thalaivar Dr. M.G. Ramachandran Central", "Government Estate", "LIC", "Thousand Lights", "AG – DMS",
         "Teynampet", "Nandanam", "Saidapet", "Little Mount", "Guindy", "Arignar Anna Alandur", "Nanganallur Road",
         "Meenambakkam", "Chennai International Airport"],
        ["Puratchi Thalaivar Dr. M.G. Ramachandran Central", "Egmore", "Nehru Park", "Kilpauk Medical College",
         "Pachaiyappa's College", "Shenoy Nagar", "Anna Nagar East", "Anna Nagar Tower", "Thirumangalam", "Koyambedu",
         "Puratchi Thalaivi Dr. J. Jayalalithaa CMBT", "Arumbakkam", "Vadapalani", "Ashok Nagar", "Ekkattuthangal",
         "Arignar Anna Alandur", "St. Thomas Mount"]

    ]

    print("-----------------------------------------Welcome to Blah Blah Blah--------------------------------------------")
    print()
    while True:
        print("Choose the city:")
        print("1. Ahmedabad")
        print("2. Hyderabad")
        print("3. Kolkata")
        print("4. Lucknow")
        print("5. Chennai")
        print("Enter 'quit' to exit")

        choice = input()

        if choice == '1':
            station = Ahmedabad
            break

        elif choice == '2':

            station = Hyderabad
            break

        elif choice == '3':

            station = Kolkata
            break

        elif choice == '4':

            station = Lucknow
            break

        elif choice == '5':

            station = Chennai
            break

        elif choice == 'quit':
            break
        else:
            print()
            print("Please choose correct option")
            print()


    if choice == 'quit':
        print("Exiting.................")
    else:
        final_station_list = get_final_list(station)
        graph = get_graph(final_station_list, station)
        source = get_source_station(final_station_list)
        dijkstra(graph, source, final_station_list)


menu()





