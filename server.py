from flask import Flask, render_template, request
import requests
import functions
app = Flask(__name__)


# Defining the home page of our site
@app.route("/", methods=['GET', 'POST'])  # this sets the route to this page
def index():
    error = None
    name = None
    message = ""
    colours  = functions.get_locations()
    if request.method == 'POST':
        id = functions.get_asset(request.form.get('upcs'))
        if id is not None: 
            if request.form.get('action1') == "CheckOut\In":
                if functions.check_out(id,functions.get_location_data(colours,request.form.get('locations'))):
                    functions.set_hardware_note(id,request.form.get('name'))
                    message = "Checked Out"
                    error = False
                elif functions.check_in(id):
                    functions.set_hardware_note(id,"")
                    message = "Checked In"
                    error = False
                else:
                    message = "Asset Not Found"
                    error = True
                    
                return render_template('index.html', form=request.form, colours=colours,message=message,error=error )
            elif request.form.get('action1') == "CheckIn":
                return render_template('index.html', form=request.form, colours=colours ) +functions.check_in(id)+" "+name
            else:
                pass # unknown
        else:
            error = "Could Not Find"
    elif request.method == 'GET':
        return render_template('index.html', form=request.form, colours=colours,error=error )
    
    return render_template('index.html', form=request.form, colours=colours )

@app.route("/checkout", methods=['GET', 'POST'])
def checkout():
    error = None
    name = None
    message = ""
    colours  = functions.get_locations()
    if request.method == 'POST':
        id = functions.get_asset(request.form.get('upcs'))
        if id is not None: 
            if request.form.get('action1') == "CheckOut\In":
                if functions.check_out(id,functions.get_location_data(colours,request.form.get('locations'))):
                    functions.set_hardware_note(id,request.form.get('name'))
                    message = "Checked Out"
                    error = False
                elif functions.check_in(id):
                    functions.set_hardware_note(id,"")
                    message = "Checked In"
                    error = False
                else:
                    message = "Asset Not Found"
                    error = True
                    
                return render_template('checkout.html', form=request.form, colours=colours,message=message,error=error )
            elif request.form.get('action1') == "CheckIn":
                return render_template('checkout.html', form=request.form, colours=colours ) +functions.check_in(id)+" "+name
            else:
                pass # unknown
        else:
            error = "Could Not Find"
    elif request.method == 'GET':
        return render_template('checkout.html', form=request.form, colours=colours,error=error )
    
    return render_template('checkout.html', form=request.form, colours=colours )
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)