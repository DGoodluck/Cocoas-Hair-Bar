from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///insta-images.db"
db = SQLAlchemy()
db.init_app(app)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(250), unique=True, nullable=False)

with app.app_context():
    db.create_all()

# Check if the script has been run before
with open('run_once.txt', 'r') as f:
    has_run = f.read()

# If the script hasn't been run before
if not has_run:
    driver = webdriver.Chrome()
    driver.get("https://greatfon.com/v/cocoashairbar")
    wait = WebDriverWait(driver, 5)

    images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".content__img-wrap a img")))
    image_list = [image.get_attribute('src') for image in images]
    driver.quit()

    with app.app_context():
        for image in image_list:
            existing_image = Image.query.filter_by(link=image).first()
            if existing_image is None:
                new_image = Image(link=image)
                db.session.add(new_image)
        db.session.commit()

    # Write to the file to indicate the script has been run
    with open('run_once.txt', 'w') as f:
        f.write('DONE')

@app.route("/")
def home():
    with app.app_context():
        result = db.session.execute(db.select(Image).order_by(Image.id))
        images = result.scalars()
        return render_template('index.html', images=images)
    
@app.route("/services")
def services():
    return render_template('services.html')
@app.route("/book-appointment")
def book():
    return render_template('book.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)