


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

# Set up logging
logger = logging.getLogger(__name__)

class GSTCalculator(APIView):
    def post(self, request):
        try:
            # Retrieve values from request data
            base_amount = request.data.get('base_amount')
            total_amount = request.data.get('total_amount')
            gst_rate = request.data.get('gst_rate')

            # Ensure gst_rate is retrieved
            if gst_rate is None:
                logger.error("GST rate is missing")
                return Response({"error": "GST rate is required"})

            # Convert to float after checking for None
            if base_amount is not None:
                base_amount = float(base_amount)
           

            results = {}

            # Exclusive GST Calculation
            if base_amount is not None:
                gst_exclusive = base_amount * (gst_rate / 100)
                total_exclusive = base_amount + gst_exclusive
                results['exclusive'] = {
                    'gst': round(gst_exclusive, 2),
                    'total_amount': round(total_exclusive, 2)
                }

           
            return Response(results, status=status.HTTP_200_OK)

        except ValueError as e:
            logger.error(f"ValueError: {e}")
            return Response({"error": "Base amount and total amount must be valid numbers"})
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return Response({"error": str(e)},)


