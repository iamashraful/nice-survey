import React from 'react'
import BaseComponent from "../components/base/BaseComponent";

export default class SurveyResponseView extends BaseComponent{
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <div>
                <h1 className="is-centered title">I am survey response view</h1>
            </div>
        )
    }
}