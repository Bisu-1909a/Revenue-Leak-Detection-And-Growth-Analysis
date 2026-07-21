import csv
import random
from datetime import datetime, timedelta


OUTPUT_FILE = "data/raw/customers.csv"
TOTAL_CUSTOMERS = 100


# -------------------------
# Name lists by gender
# -------------------------
MALE_FIRST_NAMES = [
    "Aarav", "Vivaan", "Aditya", "Arjun", "Rohan",
    "Rahul", "Ayaan", "Ishaan", "Karan", "Vikram",
    "Farhan", "Harpreet", "Samir", "Dev", "Rajesh",
    "Ritesh", "Tashi", "Lobsang", "Ritesh", "Karan"
]

FEMALE_FIRST_NAMES = [
    "Priya", "Ananya", "Sneha", "Neha", "Kavya",
    "Pooja", "Meera", "Ishita", "Nandini", "Zoya",
    "Nandini", "Pooja", "Meera", "Anjali", "Ishita"
]

OTHER_FIRST_NAMES = [
    "Alex", "Taylor", "Jordan", "Sam", "Kiran"
]

LAST_NAMES = [
    "Sharma", "Patel", "Das", "Roy", "Singh",
    "Reddy", "Nair", "Kapoor", "Banerjee", "Joshi",
    "Mishra", "Thomas", "Khan", "Verma", "Ali",
    "Bhutia", "Lepcha", "Soren", "Choudhary", "Mehta",
    "Rao", "Iyer", "Malhotra", "Varghese", "Mukherjee"
]


# -------------------------
# Regions and cities
# -------------------------
REGIONS = {
    "East": [
        "Bhubaneswar", "Cuttack", "Kolkata", "Durgapur",
        "Asansol", "Patna", "Ranchi", "Jamshedpur"
    ],
    "North": [
        "Delhi", "Noida", "Gurugram", "Chandigarh",
        "Jaipur", "Lucknow", "Dehradun", "Amritsar"
    ],
    "South": [
        "Bengaluru", "Mysuru", "Chennai", "Hyderabad",
        "Kochi", "Coimbatore", "Visakhapatnam", "Madurai"
    ],
    "West": [
        "Mumbai", "Pune", "Ahmedabad", "Surat",
        "Vadodara", "Nashik", "Panaji", "Rajkot"
    ],
    "Central": [
        "Bhopal", "Indore", "Raipur",
        "Gwalior", "Jabalpur"
    ],
    "North-East": [
        "Guwahati", "Shillong", "Agartala",
        "Aizawl", "Imphal"
    ]
}

REGION_NAMES = list(REGIONS.keys())
REGION_WEIGHTS = [20, 18, 18, 18, 14, 12]  # East, North, South, West, Central, North-East


# -------------------------
# Gender, segment, age distributions
# -------------------------
GENDERS = ["Male", "Female", "Others"]
GENDER_WEIGHTS = [53, 44, 3]

SEGMENTS = ["Retail", "Wholesale", "Distributor"]
SEGMENT_WEIGHTS = [65, 25, 10]

AGE_GROUPS = [
    (18, 25),
    (26, 35),
    (36, 50),
    (51, 80)
]
AGE_WEIGHTS = [20, 35, 30, 15]


# -------------------------
# Helper functions
# -------------------------
def generate_gender() -> str:
    """
    Generate gender using business distribution:
    Male 53%, Female 44%, Others 3%.
    """
    return random.choices(
        GENDERS,
        weights=GENDER_WEIGHTS,
        k=1
    )[0]


def generate_name(gender: str) -> str:
    """
    Generate a full name consistent with the given gender.
    """
    if gender == "Male":
        first_name = random.choice(MALE_FIRST_NAMES)
    elif gender == "Female":
        first_name = random.choice(FEMALE_FIRST_NAMES)
    else:
        first_name = random.choice(OTHER_FIRST_NAMES)

    last_name = random.choice(LAST_NAMES)
    return f"{first_name} {last_name}"


def generate_segment() -> str:
    """
    Generate customer segment:
    Retail 65%, Wholesale 25%, Distributor 10%.
    """
    return random.choices(
        SEGMENTS,
        weights=SEGMENT_WEIGHTS,
        k=1
    )[0]


def generate_region_and_city() -> tuple[str, str]:
    """
    Pick a region (with realistic weights), then a city from that region.
    """
    region = random.choices(
        REGION_NAMES,
        weights=REGION_WEIGHTS,
        k=1
    )[0]
    city = random.choice(REGIONS[region])
    return region, city


def generate_age() -> int:
    """
    Generate age based on age groups and weights.
    """
    low, high = random.choices(
        AGE_GROUPS,
        weights=AGE_WEIGHTS,
        k=1
    )[0]
    return random.randint(low, high)


def generate_signup_date() -> str:
    """
    Generate a signup date between 2024-01-01 and 2025-12-31
    in YYYY-MM-DD format (best for SQLite).
    """
    start = datetime(2024, 1, 1)
    end = datetime(2025, 12, 31)
    delta_days = (end - start).days
    random_days = random.randint(0, delta_days)
    signup_date = start + timedelta(days=random_days)
    return signup_date.strftime("%Y-%m-%d")


# -------------------------
# Main generator
# -------------------------
def main():
    with open(
        OUTPUT_FILE,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as f:
        writer = csv.writer(f)

        writer.writerow([
            "customer_id",
            "customer_name",
            "gender",
            "age",
            "city",
            "region",
            "segment",
            "signup_date"
        ])

        for customer_id in range(1, TOTAL_CUSTOMERS + 1):
            gender = generate_gender()
            name = generate_name(gender)
            age = generate_age()
            region, city = generate_region_and_city()
            segment = generate_segment()
            signup_date = generate_signup_date()

            writer.writerow([
                customer_id,
                name,
                gender,
                age,
                city,
                region,
                segment,
                signup_date
            ])

    print(f"{TOTAL_CUSTOMERS} customers generated successfully!")


if __name__ == "__main__":
    main()
