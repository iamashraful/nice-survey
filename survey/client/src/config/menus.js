import SurveyListView from "../views/SurveyListView";
import SurveyResponseView from "../views/SurveyResponseView";

const menuConfig = [
    {
        title: 'Survey',
        path: 'surveys',
        component: SurveyListView
    },
    {
        title: 'Response',
        path: 'response',
        component: SurveyResponseView
    },

]

export default menuConfig