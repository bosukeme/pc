from flask_restful import Resource
from flask import request, render_template, make_response


class PriceCheckerResource(Resource):
    
    def post(self):
        json_data = request.form.get("search_item")
        # json_data = request.get_json()
        print(json_data)

        
        try:
            from pricechecker.price_checker import start_price_checker

            result = start_price_checker(json_data)
            headers = {'Content-Type': 'text/html'}
            print(result)
            return make_response(render_template("home.html", result=result), headers)
            # return render_template('home.html', sample_input=sample_input, sample_output=sample_output), 200

        except Exception as e:
            return {
                'status': 'failed',
                'data': None,
                'message': str(e)
            }, 500






            
            