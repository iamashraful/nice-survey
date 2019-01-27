import React from 'react'
import {HashRouter as Router, Link, Route, Switch} from "react-router-dom";
import BaseComponent from "../base/BaseComponent";
import MenuConfig from '../../config/menus'
import SurveyListView from "../../views/SurveyListView";
import SurveyResponseView from "../../views/SurveyResponseView";

export default class TopNavbar extends BaseComponent {
    constructor(props) {
        super(props)
    }

    render() {
        const routerItems = MenuConfig.map((item) => {
            return (
                <Link className="navbar-item" to={item.path} key={item.path}>{item.title}</Link>
            )
        })

        return (
            <Router>
                <div>
                    <nav className="navbar is-dark" role="navigation" aria-label="main navigation">
                        <div className="navbar-brand">
                            <a role="button" className="navbar-burger burger" aria-label="menu" aria-expanded="false"
                               data-target="surveyTopNavbar">
                                <span aria-hidden="true"></span>
                                <span aria-hidden="true"></span>
                                <span aria-hidden="true"></span>
                            </a>
                        </div>

                        <div id="surveyTopNavbar" className="navbar-menu">
                            <div className="navbar-start">
                                {routerItems}
                            </div>
                        </div>
                    </nav>
                    {/*<Switch>*/}
                        {/*<Route to="/survey" component={SurveyListView}/>*/}
                        {/*<Route to="/response" component={SurveyResponseView}/>*/}
                    {/*</Switch>*/}
                    {/* Define Route(s) Here */}
                    <Switch>
                        {MenuConfig.map((item) => {
                            return (
                                <Route exact to={item.path} key={item.path} component={item.component}/>
                            )
                        })}
                    </Switch>
                </div>
            </Router>
        )
    }
}