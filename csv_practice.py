# Question 1: Csv you can do one-click automation, meaning that you can run the exact same steps on new files without having to redo everything manually compared to excel. Python can easily schedule a script to run automatically at any time wanted, loop through many different csv files, clean, and update without human interventions (Which excel cannot). Excel can easily have other poeple who do not have python installed open a file, clcik dropdown filters, adjust numbers, and view charts with out needing to download python.
# Question 2: One real world example of using the append mode is e-commerce payment and refund processing. When going into a stores check out system, everytime a customer buys an item, a payment fails, or a refund is being issued a Python script processes the transaction and appends a single timestamp to a log. It is the right tool because append guarenteens that past transactions are never accidently ereased.

# --- Exercise 2: Read and print raw rows ---
import csv

processed = []

with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
# --- Exercise 3: Skip the header ---
    header = next(reader)
    # print(header)


    # for row in reader:
    #     print(row)
   
    
# --- Exercise 4: Compute totals ---
    for row in reader:
        product, price_str, qty_str = row
        price = float(price_str)
        qty = int(qty_str)
        total = price * qty
        processed.append({"product": product, "price": price, "qty": qty, "total": total})

print(f"{'Product':<20} {'Price':>10} {'Qty':>5} {'Total':>10}")
# print(row)

for r in processed:
    print(f"{r['product']:<20} {r['price']:>10.2f} {r['qty']:>5} {r['total']:>10.2f}")

overall_total = sum(r["total"] for r in processed)
print(f"{'Overall Total':>46} {overall_total:>10.2f}")

# for item in processed:
#     print(f"{item['product']:<20} {item['price']:>10.2f} {item['qty']:>5} {item['total']:>10.2f}")
# --- Exercise 5: Filter and write ---
high_value = [r for r in processed if r["total"] > 100]

with open("data/cleaned.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for r in high_value:
        writer.writerow([r["product"], r["price"], r["qty"], f"{r['total']:.2f}"])

print(f"Wrote {len(high_value)} high_value orders to cleaned.csv")

# --- Exercise 6:csv. DictReader ---

processed_dict = []

with open("data/sales.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        qty = int(row["quantity"])
        total = price * qty
        processed_dict.append({"product": product, "price": price, "qty": qty, "total": total})

print(f"{'Product':<20} {'Price':>10} {'Qty':>5} {'Total':>10}")
for r in processed_dict:
    print(f"{r['product']:<20} {r['price']:>10.2f} {r['qty']:>5} {r['total']:>10.2f}")

overall_total_dict = sum(r["total"] for r in processed_dict)
print(f"{'Overall Total':>46} {overall_total_dict:>10.2f}")
# csv.reader returns an iterator over the rows of a csv file and each row is a list of strings. I would use this one when I have files with less columns.
# compared to csv. DictReader which is like csv.reader but returns each row as a dictionary using the first row as keys. I would prefer to use this one when when I have files with many columns. 
# --- Exercise 7: Sales summary by product

summary = {}

with open("data/sales.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        qty = int(row["quantity"])
        total = price * qty
        if product in summary:
            summary[product]["total"] += total
            summary[product]["qty"] += qty
        else:
            summary[product] = {"total": total, "qty": qty}

print(f"{'Product':<20} {'Total':>10} {'Qty':>5}")
for product, data in summary.items():
    print(f"{product:<20} {data['total']:>10.2f} {data['qty']:>5}")

# --- Exercise 8: Append mode log ---
from datetime import datetime

total_revenue = 0.0

with open ("data/sales.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total_revenue += float(row["price"]) * int(row["quantity"])

timestamp = datetime.now()
log_entry = f"{timestamp}: Total revenue generated: ${total_revenue:.2f}\n"

with open("data/run_log.txt", "a") as f:
    f.write(log_entry)

print("Logged:", log_entry)