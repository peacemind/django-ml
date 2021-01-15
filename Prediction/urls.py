from django.urls import path
import Prediction.views as views

urlpatterns = [
    # function based view
    path('add/', views.api_add, name = 'api_add'),
    # class based view
    path('add_values/', views.Add_Values.as_view(), name = 'api_add_values'),
    # iris prediction
    path('predict/', views.IRIS_Model_Predict.as_view(), name = 'predict'),
]